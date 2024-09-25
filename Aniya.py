input_data = open('input.txt', 'r') 
N= input_data.read() 

N = N.split() 
a = int(N[0])
b = int(N[1])
c = int(N[2])
out=(int(a)*int(b)*int(c))*2

output_data = open('output.txt', 'w') 
output_data.write (str(out))

input_data.close() 
output_data.close()