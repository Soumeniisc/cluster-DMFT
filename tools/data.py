import numpy as np
from numpy import *
import matplotlib.pyplot as plt
data = np.loadtxt("super_states.text")
print sum(data[:,4]) #256 = 4^4 which is the dimension of the total hilbert space for hubbard model. for t-J model it is 81= 3^4

#plt.plot(np.arange(len(data[:,0])), data[:,4])
#plt.show()

Sig_ori= loadtxt("Sig.out")
Sig= loadtxt("Sig.out.9")

plt.plot(Sig_ori[:,0],Sig_ori[:,1],'-o',label="orinal")
plt.plot(Sig[:,0],Sig[:,1],'-o', label  = "calculated_by+me")
plt.legend()
plt.savefig("Sig_0_0.eps",format="eps")
plt.show()

plt.plot(Sig_ori[:,0],Sig_ori[:,1],'-o',label="0_0")
plt.plot(Sig_ori[:,0],Sig_ori[:,3],'-o', label  = "0_pi")
plt.plot(Sig_ori[:,0],Sig_ori[:,5],'-o', label  = "pi_pi")
plt.legend()
plt.xlim(0,10)
plt.savefig("Sig_real.eps",format="eps")
plt.show()

plt.plot(Sig_ori[:,0],Sig_ori[:,2],'-o',label="0_0")
plt.plot(Sig_ori[:,0],Sig_ori[:,4],'-o', label  = "0_pi")
plt.plot(Sig_ori[:,0],Sig_ori[:,6],'-o', label  = "pi_pi")
plt.legend()
plt.xlim(0,10)
plt.savefig("Sig_imag.eps",format="eps")
plt.show()





