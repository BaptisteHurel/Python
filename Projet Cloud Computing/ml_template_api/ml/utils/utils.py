# class DataHandler
class DataHandler:
    """
        Getting data from bucket
    """
    def __init__(self):
        """
            Initialising the 3 datasets :
            entry 1
            entry 2
            result
        """
        print("DataHandlerintialisation")
        self.df_lf = None
        self.df_pa = None
        self.df_res = None
        print("intialisation done")

    def get_data(self):
        print("loading data from bucket")
        self.df_lf = pd.read_csv("seasons_stats.csv",sep=';')
        self.df_pa = pd.read_csv("seasons_stats.csv",sep=';')
        print("data loaded from bucket")

    def group_data(self):
        print("merging data")
        self.df_res = pd.merge(self.df_lf,self.df_pa.groupby('Player')['Tm'].mean('PTS'),how='inner', on='Player')
        print("size of the merged data : {} lines, {} columns".format(self.df_res.shape[0],self.df_res.shape[1]))

    def get_process_data(self):
        self.get_data()
        self.group_data()
        print("end of processing\n")

# class FeatureRecipe
class FeatureRecipe:
    
    def __init__(self, data: pds.DataFrame):
        print("FeatureRecipe starts...")
        self.df = data
        self.cate = []
        self.floa = []
        self.intt = []
        print("End of FeatureRecipe initialisation\n")
    
    def separate_variable_types(self) -> None:
        print("Separate variable types starts...")
        for col in self.df.columns:
            if self.df[col].dtypes == int:
                self.intt.append(self.df[col])
            elif self.df[col].dtypes == float:
                self.floa.append(self.df[col])
            else:
                self.cate.append(self.df[col])
        print("Separate variable types end...")
        print ("Dataset number of columns : {} \nnumber of discreet values : {} \nnumber of continuous values : {} \nnumber of others : {} \ntotal size : {}\n".format(len(self.df.columns),
        len(self.intt),len(self.floa),len(self.cate),len(self.intt)+len(self.floa)+len(self.cate) ))
        
    def drop_uselessf(self):
        print("Drop useless feature start...")
        
        if "Unnamed: 0" in self.df.columns:
            self.df.drop("Unnamed: 0", axis=1, inplace=True)
            
        for col in self.df.columns:
            if self.df[col].isna().sum() == len(self.df[col]):
                self.df.drop([col], axis=1, inplace=True)
                
        print("Drop useless feature end...")
        print("Number columns remaining {}\n".format(len(self.df.columns)))
        
    def deal_duplicate(self):
        print("Deal duplicate start...")
        dropped_duplicates = self.df.drop_duplicates(inplace=True)
        print("Dropped duplicates : {}".format(dropped_duplicates))
        print("Deal duplicate end...")
    
    def drop_nanp(self, thresold: float):
        """
        Drop NaN columns according to a thresold
        """
        def deal_nanp(df:pd.DataFrame, thresold: float):
            bf=[]
            for c in self.data.columns.to_list():
                if self.data[c].isna().sum()/self.data.shape[0] > thresold:
                    bf.append(c)
            logging.debug("{} feature have more than {} NaN ".format(len(bf), thresold))
            logging.debug('\n\n - - - features - - -  \n {}'.format(bf))
            return bf 
        self.data = self.data.drop(deal_nanp(self.data, thresold), axis=1)
        logging.debug('Some NaN features droped according to {} thresold'.format(thresold))
    
    def get_duplicates(self):
        print("Get duplicates")
        
        for col in self.df.columns:
            for row in range(self.df.shape[0]):
                        
    def deal_dtime(self):
        pass
    
    def prepare_data(self, threshold: float):
        self.drop_uselessf()
        self.separate_variable_types()
        self.deal_duplicate()
        self.drop_nanp(threshold)
        self.deal_dtime()

# class FeatureExtractor
class FeatureExtractor:
    """
    Feature Extractor class
    """
    def __init__(self, data: pd.DataFrame, flist: list):
        """
            Input : pandas.DataFrame, feature list to drop
            Output : X_train, X_test, y_train, y_test according to sklearn.model_selection.train_test_split
        """
        self.X_train, self.X_test, self.y_train, self.y_test = None,None,None,None
        self.df = data
        self.flist = flist
        
    def splitting(size:float,rng:int,X pd.Series):
        self.X_train, self.X_test, self.y_train, self.y_test train_test_split(X, y, size, rng)
        
    def train():
        pass

# class ModelBuilder
class ModelBuilder:
    """
        Class for train and print results of ml model 
    """
    def __init__(self, model_path: str = None, save: bool = None):
        pass
    def __repr__(self):
        pass
    def predict(self, X) -> np.ndarray:
        pass
    def save_model(self, path:str):
        #with the format : 'model_{}_{}'.format(date)
        pass
    def load_model(self):
        try:
            #load model
            pass
        except:
            pass