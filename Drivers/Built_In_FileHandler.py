'''
Created on Mar 25, 2017

@author: RizDesktop
'''
import sys
from Framework.Utilities import CommonUtil

def delete_folder(dependency,run_params,step_data,file_attachment,temp_q):
    try:
        sTestStepReturnStatus = Selenium_Built_In.delete_folder(dependency)
        return CommonUtil.Result_Analyzer(sTestStepReturnStatus,temp_q)
    except Exception:
        return CommonUtil.Exception_Handler(sys.exc_info(), temp_q)