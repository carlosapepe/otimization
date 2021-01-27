#from os import name
# encoding: utf-8

from lp_solve import * #impor of lpsolve 
## -------------------------------------------------------------------------------
# Criado por Carlos Alberto Pedroso
# Data: 21/12/2020
# Para disciplina de Otimização (trabalho 1)
# Professor André Guedes 
## -------------------------------------------------------------------------------
## -------------------------------------------------------------------------------
## Recebe valores de  #Tarefas e #Máquina
## -------------------------------------------------------------------------------
def main ():
    while True:
        value = raw_input("Entre com valores para Tarefas e Máquinas separados:\n")
        newvalue = value.split()
        if len(newvalue) == 2 and int(newvalue[0]) > 0 and int(newvalue[1]) > 0 :
            break
        print ("A entrada deve conter dois valores validos maior que 0 para Tarefas e Maquinas \n")
            #quit()
    nTarefas = int (newvalue[0])
    mMaquinas = int(newvalue[1])

    ## -------------------------------------------------------------------------------
    ## Rece as horas de cada tarefa
    ## -------------------------------------------------------------------------------

    list_h_tasks=[]
    for i in range( int(nTarefas)):
        while True:
            horas =  int(raw_input("Entre com as horas para cada tarefa "+str(i+1)+":\n"))  
            if horas > 0:
                list_h_tasks.append(horas)
                break 
            print ("A horas das tarefas devem ser maior que 0\n")

    ## -------------------------------------------------------------------------------
    ## Recebe custo e tempo máximo para cada máquina
    ## -------------------------------------------------------------------------------

    list_custos=[] # lista de custo para cada máquina
    list_h_maquinas=[] # lista de horas para cada máquina
    while True:
        for i in range( int(mMaquinas)):
            listn = raw_input("Entre com os custos e tempo máximo para cada máquina "+str(i+1)+":\n")
            newList = listn.split()
            list_custos.append(int (newList[0]))
            list_h_maquinas.append(int (newList[1]))
        if sum(list_h_maquinas) >= sum(list_h_tasks): 
            break 
        print ("Os valores devem ser maior que 0 para funcionar\n")       

    ## -------------------------------------------------------------------------------
    ## Leia o custo e o tempo máximo de cada máquin
    ## loop externo controlado por máquinas e loop interno controlado por Tarefas
    ## -------------------------------------------------------------------------------

    list_nt_maquinas=[] ## Lista para o número de tarefas de cada máquina
    list_t_maquinas=[]## Lista de tarefas por cada máquina
    for i in range(int(mMaquinas)):
        while True:
            soma1 = int(raw_input("Por favor, insira o número de tarefas atribuídas à máquina "+str(i+1)+":\n"))
            if soma1  > 0:
                break
            print ("Os valores não devem ser mais do que o número da tarefa\n")
        ## Read the number o tasks assigned to a machine
        list_nt_maquinas.append(soma1)
        list_t_maquinas.append([])
        for j in range(int(list_nt_maquinas[i])):
            ## Read the tasks assigned to a Machine
            number = raw_input("Entre com as tarrefas "+str(j+1)+" Por máquina "+str(i+1)+":\n")
            list_t_maquinas[i].append(number)

    #--------------------------------------------------------------------------------------
    #For para criar o vetor f de coeficientes para a função objetivo
    #--------------------------------------------------------------------------------------    
    list_f =[]
    for i in range( int(mMaquinas)):
        for j in range( int(nTarefas)):
            x = -int (list_custos[i])
            list_f.append(x)
    #---------------------------------------------------------------------------------------        
    # Conjunto de For para criar a matriz com n x m representando as restrições lineares
    #--------------------------------------------------------------------------------------- 
    list_a=[]
    for i in range( int(mMaquinas) + int(nTarefas)):
        list_a.append([])
        for j in range( int(mMaquinas) * int(nTarefas)):
            list_a[i].append(0)

    for i in range( int(mMaquinas)):
        for j in range( int(nTarefas)):
            list_a[i][j + nTarefas*i] = 1   	

    for i in range(int(nTarefas)):
        for j in range( (int(mMaquinas) )):
            list_a[i + int(mMaquinas)][i + nTarefas*j] = 1
                    
    #--------------------------------------------------------------------------------------- 
    # For para criar o vetor de variáveis inteiras. Pode ser omitido ou vazio e
    # vetor n de limites inferiores não negativos podendo ser vazio ou omitido
    #--------------------------------------------------------------------------------------- 
    list_xint=[]
    list_vlb=[]
    for i in range( int(mMaquinas) * int(nTarefas)):
            list_xint.append(i+1)
            list_vlb.append(0)
    #--------------------------------------------------------------------------------------- 

    #--------------------------------------------------------------------------------------- 
    #vetor m que determina o sentido das desigualdades:
    #   e(i) <-1  ==> menor 
    #   e(i) = 0  ==> igual
    #   e(i) > 1  ==> maior  
    #---------------------------------------------------------------------------------------             
    list_b=[]
    list_e=[]
    for i in range( int (mMaquinas)):
        list_b.append( int (list_h_maquinas[i]))         
        list_e.append(-1)   

    for i in range( int (nTarefas)):
        list_b.append( int (list_h_tasks[i]))
        list_e.append(0)   
    #--------------------------------------------------------------------------------------- 

    #---------------------------------------------------------------------------------------      
    # print para vertificação do preenchimento dos campos no lpsolve 
    # print ("f: ")      
    # print (list_f)
    # print ("\na: ") 
    # print (list_a)
    # print ("\nb: ") 
    # print (list_b)
    # print ("\ne: ") 
    # print (list_e)
    # print ("\nvlb: ") 
    # print (list_vlb)
    # print ("\nxint: ")  
    # print (list_xint)
    #--------------------------------------------------------------------------------------- 

    #--------------------------------------------------------------------------------------- 
    # construção e preenchimento do dos campos do lpsolve 
    [obj, x, duas] = lp_solve(list_f, list_a, list_b, list_e, list_vlb, None, None, 0)
    resul = (0.0 if obj == 0 else obj*-1)
    #---------------------------------------------------------------------------------------
    #---------------------------------------------------------------------------------------
    #imprimindo o resultado
    count = 0
    for i in range( int (mMaquinas * nTarefas)):
        if count == nTarefas: 
            print ("")
            count = 0
        if isinstance(x, list):
	     print (x [i]),
        else :
	    print (x),
        #print (x [i]),
        #print (x),
        count += 1
    print ("")
    print resul
    #--------------------------------------------------------------------------------------- 
