# import pandas
#
#
# from scipy import stats
#
# import statsmodels.api as sm
# import statsmodels.formula.api as smf

# def anova(self):
#     y1, y2, y3 = [], [], []
#
#     for cvs, dist in zip(self.stats["customer_view_size"], self.stats["delta_position"]):
#         if cvs == 3:
#             y1.append(dist)
#         elif cvs == 7:
#             y2.append(dist)
#         else:
#             y3.append(dist)
#
#     # df = pandas.DataFrame.from_dict(self.stats)
#     # mod = smf.ols('delta_position ~ customer_view_size',
#     #          data=df).fit()
#
#     # aov_table = sm.stats.anova_lm(mod, typ=3)
#     # print(aov_table)
#
#     f_val, p_val = stats.f_oneway(y1, y2, y3)
#     print(f_val, p_val)
#
#     # def linear_regression(self, var1, var2):
#     #
#     #     slope, intercept, r_value, p_value, std_err = stats.linregress(
#     #         self.stats[var1], self.stats[var2])
#     #
#     #     print("LR {} ~ {}: {} [p={}]".format(var1, var2, r_value, p_value))
#     #
#     # def multiple_regression_analysis(self):
#     #
#     #     print("Multiple regression analysis")
#     #     df = pandas.DataFrame.from_dict(self.stats)
#     #     lm = smf.ols(formula="delta_position ~ customer_view_size + transportation_cost", data=df).fit()
#     #     # lm = smf.ols(formula="delta_price ~ customer_view_size", data=df).fit()
#     #     print(lm.params)
#     #
#     # def regression_analysis(self):
#     #
#     #     for i, j in [
#     #         ("customer_view_size", "delta_position"),
#     #         ("customer_view_size", "delta_price"),
#     #         ("customer_view_size", "profit"),
#     #         ("delta_position", "delta_price"),
#     #         ("delta_position", "profit"),
#     #         # ("transportation_cost", "delta_position"),
#     #         # ("transportation_cost", "delta_price")
#     #     ]:
#     #         self.scatter_plot(var1=i, var2=j)
#     #         self.linear_regression(var1=i, var2=j)