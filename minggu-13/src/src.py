#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


s = pd.Series([1, 3, 5, np.nan, 6, 8])


# In[4]:


s


# In[5]:


dates = pd.date_range("20130101", periods=6)


# In[6]:


dates


# In[7]:


df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))


# In[8]:


df


# In[9]:


df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)


# In[10]:


df2


# In[11]:


df2.dtypes


# In[12]:


df2.<TAB>  # noqa: E225, E999


# In[13]:


df.head()


# In[14]:


df.tail(3)


# In[15]:


df.index


# In[16]:


df.columns


# In[17]:


df.to_numpy()


# In[18]:


df2.to_numpy()


# In[19]:


df.describe()


# In[20]:


df.T


# In[21]:


df.sort_index(axis=1, ascending=False)


# In[22]:


df.sort_values(by="B")


# In[23]:


df["A"]


# In[24]:


df[0:3]


# In[25]:


df["20130102":"20130104"]


# In[26]:


df.loc[dates[0]]


# In[27]:


df.loc[:, ["A", "B"]]


# In[28]:


df.loc["20130102":"20130104", ["A", "B"]]


# In[29]:


df.loc["20130102", ["A", "B"]]


# In[30]:


df.loc[dates[0], "A"]


# In[31]:


df.at[dates[0], "A"]


# In[32]:


df.iloc[3]


# In[33]:


df.iloc[3:5, 0:2]


# In[34]:


df.iloc[[1, 2, 4], [0, 2]]


# In[35]:


df.iloc[1:3, :]


# In[36]:


df.iloc[:, 1:3]


# In[37]:


df.iloc[1, 1]


# In[38]:


df.iat[1, 1]


# In[39]:


df[df["A"] > 0]


# In[40]:


df[df > 0]


# In[41]:


df2 = df.copy()


# In[42]:


df2["E"] = ["one", "one", "two", "three", "four", "three"]


# In[43]:


df2


# In[44]:


df2[df2["E"].isin(["two", "four"])]


# In[45]:


s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))


# In[46]:


s1


# In[47]:


df["F"] = s1


# In[48]:


df.at[dates[0], "A"] = 0


# In[49]:


df.iat[0, 1] = 0


# In[50]:


df.loc[:, "D"] = np.array([5] * len(df))


# In[51]:


df


# In[52]:


df2 = df.copy()


# In[53]:


df2[df2 > 0] = -df2


# In[54]:


df2


# In[55]:


df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])


# In[56]:


df1.loc[dates[0] : dates[1], "E"] = 1


# In[57]:


df1


# In[58]:


df1.dropna(how="any")


# In[59]:


df1.fillna(value=5)


# In[60]:


pd.isna(df1)


# In[61]:


df.mean()


# In[62]:


df.mean(1)


# In[63]:


s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)


# In[64]:


s


# In[65]:


df.sub(s, axis="index")


# In[66]:


df.apply(np.cumsum)


# In[67]:


df.apply(lambda x: x.max() - x.min())


# In[68]:


s = pd.Series(np.random.randint(0, 7, size=10))


# In[69]:


s


# In[70]:


s.value_counts()


# In[71]:


s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])


# In[72]:


s.str.lower()


# In[73]:


df = pd.DataFrame(np.random.randn(10, 4))


# In[74]:


df


# In[75]:


pieces = [df[:3], df[3:7], df[7:]]


# In[76]:


pd.concat(pieces)


# In[77]:


left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})


# In[78]:


right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})


# In[79]:


left


# In[80]:


right


# In[81]:


pd.merge(left, right, on="key")


# In[82]:


left = pd.DataFrame({"key": ["foo", "bar"], "lval": [1, 2]})


# In[83]:


right = pd.DataFrame({"key": ["foo", "bar"], "rval": [4, 5]})


# In[84]:


left


# In[85]:


right


# In[86]:


pd.merge(left, right, on="key")


# In[87]:


df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)


# In[88]:


df


# In[89]:


df.groupby("A").sum()


# In[90]:


df.groupby(["A", "B"]).sum()


# In[91]:


tuples = list(
    zip(
        *[
            ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
            ["one", "two", "one", "two", "one", "two", "one", "two"],
        ]
    )
)


# In[92]:


index = pd.MultiIndex.from_tuples(tuples, names=["first", "second"])


# In[93]:


df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])


# In[94]:


df2 = df[:4]


# In[95]:


df2


# In[96]:


stacked = df2.stack()


# In[97]:


stacked


# In[98]:


stacked.unstack()


# In[99]:


stacked.unstack(1)


# In[100]:


stacked.unstack(0)


# In[101]:


df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    }
)


# In[102]:


df


# In[103]:


pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"])


# In[104]:


rng = pd.date_range("1/1/2012", periods=100, freq="S")


# In[105]:


ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)


# In[106]:


ts.resample("5Min").sum()


# In[107]:


rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")


# In[108]:


ts = pd.Series(np.random.randn(len(rng)), rng)


# In[109]:


ts


# In[110]:


ts_utc = ts.tz_localize("UTC")


# In[111]:


ts_utc


# In[112]:


ts_utc.tz_convert("US/Eastern")


# In[113]:


rng = pd.date_range("1/1/2012", periods=5, freq="M")


# In[114]:


ts = pd.Series(np.random.randn(len(rng)), index=rng)


# In[115]:


ts


# In[116]:


ps = ts.to_period()


# In[117]:


ps


# In[118]:


ps.to_timestamp()


# In[119]:


prng = pd.period_range("1990Q1", "2000Q4", freq="Q-NOV")


# In[120]:


ts = pd.Series(np.random.randn(len(prng)), prng)


# In[121]:


ts.index = (prng.asfreq("M", "e") + 1).asfreq("H", "s") + 9


# In[122]:


ts.head()


# In[123]:


df = pd.DataFrame(
    {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]}
)


# In[124]:


df["grade"] = df["raw_grade"].astype("category")


# In[125]:


df["grade"]


# In[126]:


df["grade"].cat.categories = ["very good", "good", "very bad"]


# In[127]:


df["grade"] = df["grade"].cat.set_categories(
    ["very bad", "bad", "medium", "good", "very good"]
)


# In[128]:


df["grade"]


# In[129]:


df.sort_values(by="grade")


# In[130]:


df.groupby("grade").size()


# In[131]:


import matplotlib.pyplot as plt


# In[132]:


plt.close("all")


# In[133]:


ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))


# In[134]:


ts = ts.cumsum()


# In[135]:


ts.plot()


# In[136]:


df = pd.DataFrame(
    np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]
)


# In[137]:


df = df.cumsum()


# In[138]:


plt.figure()


# In[139]:


df.plot()


# In[140]:


plt.legend(loc='best')


# In[141]:


df.to_csv("foo.csv")


# In[142]:


pd.read_csv("foo.csv")


# In[143]:


df.to_hdf("foo.h5", "df")


# In[144]:


pd.read_hdf("foo.h5", "df")


# In[145]:


df.to_excel("foo.xlsx", sheet_name="Sheet1")


# In[146]:


pd.read_excel("foo.xlsx", "Sheet1", index_col=None, na_values=["NA"])


# In[ ]:




