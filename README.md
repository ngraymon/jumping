# Fermionic Neural Network: PHYS 449 Final Project
This projects goal is to replicate the algorithm and experiments defined in 
"Ab-Initio Solution of the Many-Electron Schroedinger Equation with Deep Neural Networks", David Pfau, James S. Spencer, Alex G de G Matthews and W.M.C. Foulkes, Phys. Rev. Research 2, 033429 (2020).
\
The objective of the FermiNet is to create the optimal trial Ansatz for spin systems that obeys 
Fermi-Dirac statistics. The FermiNet uses no data other than atomic positions and charges.


## Running The FermiNet
To run and train the FermiNet, use the `driver.py` file, run
```
python driver.py --name NAME --length LENGTH -- param PARAM.json -res-path RESULT PATH -n N -v V
```
for more information on the arguments use,
```
python driver.py --h
```
If arguments are not provided the default values for the arguments are as follows,
```
--name hydrogen
--length 1
--param param.json
-res-path results
-n 12
-v 1
```

## Contributors
* Andrew Francey
* Jean-Baptiste Valentin
* Matthew Waters
* Neil Goerge Raymond
* Willian Archer

## Original GitHub repository
The FermiNet was created by David Pfau, James S. Spencer, Alex G de G Matthews 
and W.M.C. Foulkes. Described in 
This github is based off the original github which can be found at,
https://github.com/deepmind/ferminet