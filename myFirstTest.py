#!/usr/bin/env python -u
# encoding: utf-8
'This is my first TestAutomation test!'
  
from __future__ import print_function, unicode_literals, absolute_import, division
  
import testautomationextras as tae

tae.meta_data(
    Environment={
        'Virtualenv': {
            'RequiredPackages': {
                'testautomationextras': ''
            }
        }
    }
)
 
def main(_):
    'main'
    print('hello world!')
 
 
if __name__ == '__main__':
    with tae.context() as c:
        main(c)
