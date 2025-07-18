import os
import Data_colector as dc
import pandas as pd
class app():
    
        Action_df = pd.DataFrame(dc.grup_action_data())
        Action_df.to_csv("Actions10y.CSV")
   

if __name__ == "__app__":
    app() 