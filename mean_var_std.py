import numpy as np

#012
#345(list
#678
def calculate(lista): 
  if len(lista) !=9: 
    raise ValueError('List must contain nine numbers.')
    return 'Wrong input'
  #If the user has not typed 9 numbers the input is unsuitable.
  else: 
    matrix=np.array(lista) #Conver out list to array
    #The word lista derives from Greek language and means λιστ.
    #print(matrix)
    #Measuring the averages.
    mean_axis2=[(matrix[0:3].mean()),(matrix[3:6].mean()),(matrix[6:].mean())] #rows
    mean_axis1=[(matrix[[0,3,6]].mean()),(matrix[[1,4,7]].mean()),(matrix[[2,5,8]].mean())] #col
    mean_flattened=(matrix[:].mean())
    #print(mean_flattened)
    #Measuring the variances.
    var_axis2=[(matrix[0:3].var()),(matrix[3:6].var()),(matrix[6:].var())]
    var_axis1=[(matrix[[0,3,6]].var()),(matrix[[1,4,7]].var()),(matrix[[2,5,8]].var())]
    var_flattened=(matrix[:].var())
    #Measuring standard deviations.
    std_axis2=[(matrix[0:3].std()),(matrix[3:6].std()),(matrix[6:].std())]
    std_axis1=[(matrix[[0,3,6]].std()),(matrix[[1,4,7]].std()),(matrix[[2,5,8]].std())]
    std_flattened=(matrix[:].std())
    #Measuring the maximums.
    max_axis2=[(matrix[0:3].max()),(matrix[3:6].max()),(matrix[6:].max())]
    max_axis1=[(matrix[[0,3,6]].max()),(matrix[[1,4,7]].max()),(matrix[[2,5,8]].max())]
    max_flattened=(matrix[:].max())
    #Measuring the minimums.
    min_axis2=[(matrix[0:3].min()),(matrix[3:6].min()),(matrix[6:].min())]
    min_axis1=[(matrix[[0,3,6]].min()),(matrix[[1,4,7]].min()),(matrix[[2,5,8]].min())]
    min_flattened=(matrix[:].min())
    #Measuring the sums.
    sum_axis2=[(matrix[0:3].sum()),(matrix[3:6].sum()),(matrix[6:].sum())]
    sum_axis1=[(matrix[[0,3,6]].sum()),(matrix[[1,4,7]].sum()),(matrix[[2,5,8]].sum())]
    sum_flattened=(matrix[:].sum())
    print(sum_flattened)

  return {'mean': [mean_axis1, mean_axis2, mean_flattened],'variance': [var_axis1,var_axis2, var_flattened],'standard deviation': [std_axis1, std_axis2, std_flattened],'max': [max_axis1,max_axis2, max_flattened],'min': [min_axis1, min_axis2, min_flattened],'sum': [sum_axis1, sum_axis2, sum_flattened] }



#return calculations