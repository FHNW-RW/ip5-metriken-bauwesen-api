import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

import src.package.consts as c

usage_wohnen_mfh = ['WOHNBAUTEN__MFH_HIGH', 'WOHNBAUTEN__MFH_MEDIUM', 'WOHNBAUTEN__MFH_LOW']
usage_wohnen_efh = ['WOHNBAUTEN__EFH_REIHEN_LOW', 'WOHNBAUTEN__EFH_REIHEN_MEDIUM', 'WOHNBAUTEN__EFH_REIHEN_HIGH']
other_usages = ['ANDERES', 'OFFENE_BAUTEN', 'TECHNIK', 'IRRELEVANT', 'AUSSENANLAGEN']


def combine_usage(usage_main, usage_cluster):
    if usage_main in usage_wohnen_efh:
        return 'WOHNEN_EFH'
    elif usage_cluster in usage_wohnen_efh:
        return 'WOHNEN_MFH'
    elif usage_cluster in other_usages:
        # TODO: remove completely?
        return 'ANDERS'
    else:
        return usage_cluster


class CombineFeatures(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self  # nothing else to do

    def transform(self, X, y=None):
        # calculate HNF / GF ratio
        X[c.FIELD_HNF_GF_RATIO] = X.eval(f'{c.FIELD_AREA_MAIN_USAGE} / {c.FIELD_AREA_TOTAL_FLOOR_416}')

        # combine usage cluster with main usage
        X[c.FIELD_COMBINED_USAGE] = X.apply(
            lambda x: combine_usage(x[c.FIELD_NOM_USAGE_MAIN], x[c.FIELD_USAGE_CLUSTER]), axis=1
        )

        return X


class NumericalImputer(BaseEstimator, TransformerMixin):

    def __init__(self, cluster_mean_values, field=c.FIELD_VOLUME_TOTAL_416, other=c.FIELD_VOLUME_TOTAL_116,
                 drop_other=True):
        self.field = field
        self.other = other
        self.drop_other = drop_other
        self.cluster_mean_values = cluster_mean_values

    def fit(self, X, y=None):
        return self  # nothing else to do

    def transform(self, X, y=None):
        X = X.groupby(c.FIELD_USAGE_CLUSTER).apply(
            lambda x: self.__apply_cluster_mean(x, x[c.FIELD_USAGE_CLUSTER].iloc[0]))

        if self.drop_other:
            X = X.drop(columns=[self.other])

        return X

    def __apply_cluster_mean(self, grp, grp_name):
        factor = self.cluster_mean_values[grp_name]
        grp[self.field] = grp[self.field].fillna(grp[self.other] * float(factor))

        return grp

    @staticmethod
    def __apply_mean(df, field, other, factor):
        df[field] = df[field].fillna(df[other] * float(factor))


class OneHotEncodingTransformer(BaseEstimator, TransformerMixin):

    def __init__(self, field):
        self.field = field
        self.encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)

    def fit(self, X, y=None):
        self.encoder.fit(X[[self.field]])
        return self

    def transform(self, X, y=None):
        # Create a Pandas DataFrame of the hot encoded column
        transformed = self.encoder.transform(X[[self.field]])
        ohe_df = pd.DataFrame(transformed, columns=self.encoder.get_feature_names())

        # concat with original data and remove field
        X = pd.concat([X, ohe_df], axis=1).drop([self.field], axis=1)

        return X


class LabelEncoderTransformer(BaseEstimator, TransformerMixin):

    def __init__(self, field):
        self.field = field
        self.encoder = LabelEncoder()

    def fit(self, X, y=None):
        self.encoder.fit(X[[self.field]])
        return self

    def transform(self, X, y=None):
        X[self.field] = self.encoder.transform(X[[self.field]])

        return X
