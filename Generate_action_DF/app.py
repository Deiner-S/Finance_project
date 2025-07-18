from DataColector import DataColector
import pandas as pd
class app():
        data_colector = DataColector()
        Action_df = pd.DataFrame(data_colector.grup_action_data())
        Action_df.to_csv("Actions10y.CSV")
   

if __name__ == "__app__":
    app() 