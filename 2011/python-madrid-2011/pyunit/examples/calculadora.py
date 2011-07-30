#!/usr/bin/env python
# -*- coding: utf-8 -*- 

class Calculadora:
    def suma(self,num1,num2):
        return num1+num2

    def resta(self,num1,num2):
        return num1-num2

    def multiplica(self,num1,num2):
        return num1*num2

    def divide(self,num1,num2):
        if num1!=0 and num2==0:
            return "infinito"
        elif num1==0 and num2==0:
            return "indeterminación"
        return num1/num2
