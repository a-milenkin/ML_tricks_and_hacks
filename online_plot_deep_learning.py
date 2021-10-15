from IPython import display
import time
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

def real_plot(epoch_acc_hist):
    #loss, acc, val_loss, val_acc = zip(*history)
  # acc, val_acc = history
    plt.figure(figsize=(15, 9))
    #plt.plot(acc, label="train_acc")
    #print('----------------')
    plt.plot(epoch_acc_hist, label="val_acc")
    plt.legend(loc='best')
    plt.xlabel("epochs")
    plt.ylabel("acc")
    plt.show()
    display.clear_output(wait=True)
    time.sleep(2)
