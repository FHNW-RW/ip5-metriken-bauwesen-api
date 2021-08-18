import pandas as pd
from sklearn.base import TransformerMixin
from sklearn.preprocessing import OneHotEncoder

import src.package.consts as c


class VolumeImputer(TransformerMixin):

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
        # use ANDERES for unknown group
        if grp_name not in self.cluster_mean_values:
            grp_name = 'ANDERES'

        factor = self.cluster_mean_values[grp_name]
        grp[self.field] = grp[self.field].fillna(grp[self.other] * float(factor))

        return grp

    @staticmethod
    def __apply_mean(df, field, other, factor):
        df[field] = df[field].fillna(df[other] * float(factor))


class OneHotEncodingTransformer(TransformerMixin):

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
