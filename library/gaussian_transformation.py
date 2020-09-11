from scipy.stats import boxcox
import seaborn as sns 


def log_transform(df,feature):
	bx=np.log(df[feature]+1)
	return pd.DataFrame(bx)


def reciprocal_transform(df,feature):
	bx=1/(df[feature]+1)
	return pd.DataFrame(bx)


def square_root_transform(df,feature):
	bx=df[feature]**(1/2)
	return pd.DataFrame(bx)


def exponential_transform(df,feature):
	bx=df[feature]**(1/5)
	return pd.DataFrame(bx)


def boxcox_transform(df,feature):
	bx,parameter=boxcox(df[feature])
	return bx


def box_plot(df,feature):
	sns.boxplot(df[feature])