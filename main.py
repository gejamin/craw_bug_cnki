import requests
import pandas as pd
import process_single
import multiprocessing


journal_name=pd.read_csv('./links/搜索链接.csv')


def main():
    journal_name_index=1
    pool=multiprocessing.Pool(journal_name.shape[0])
    for journal_code in journal_name.iloc[1:, 1]:
        pool.apply_async(process_single.process_single,args=(journal_code,journal_name.iloc[journal_name_index,0]))
        journal_name_index+=1
    pool.close()
    pool.join()

if __name__ == '__main__':
    main()