'''
Created on 2017年3月13日

@author: 36163
'''

class Assert(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
    def assertMethod(self,assertData,fail_msg):
        if assertData == 'assertEqual': #
            self.assertEqual(assertData,fail_msg)
        elif assertData == 'assertNotEqual':
            self.assertNotEqual(assertData,fail_msg)
        elif assertData == 'assertIsNotNone':  #元素不存在，则pass
            self.assertIsNotNone(assertData,fail_msg)
        else:
            pass
            
            