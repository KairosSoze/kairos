## Step-by-step guide for running code files
## (Note - some files omit small but key details for final implementation! These challenges can be resolved relatively easily with critical thinking and  human-AI collabortion. This was intentional. We aim to encourage critical thought at every stage of the process). ## 

## 1. Introduction ##

This guide is intended to help you understand, utilize and contribute to the protein folding project. 
It provides step-by-step instructions for setting up the environment, running the code and interpreting the results.
It also offers insights into the design choices and the underlying principles behind the quantum-enhanced protein folding algorithm.
The protein folding algorithm is implemented in Python and utilizes the Qiskit library for quantum computation. 
It consists of several code files, each responsible for a specific aspect of the folding process. 
Each individual file can be viewed in the Project Directory on the left of the page.

  1. Quantum Encoding: Encodes the amino acid sequence into a quantum circuit.
  2. Entanglement Layer: Generates entanglement between the qubits representing the amino acids.
  3. Energy Minimization: Performs energy minimization to find the most stable protein structure.
  4. Intuitive Layer: Incorporates intuitive pattern recognition into the folding process.
  5. Measurement and Interpretation: Measures the qubits and interprets the results to predict the protein's 3D structure.
  6. Additional Modules: Includes data loading, quantum circuit optimization, visualization tools, evaluation metrics, and error mitigation.

## 2. Setting Up the Environment ##

Before running the code, you'll need to set up a Python environment with the necessary dependencies. Here's a step-by-step guide:
  1. Install Python: If you don't already have Python installed, download and install the latest version from the official Python website: https://www.python.org/downloads/  
  2. Create a Virtual Environment: It's recommended to create a virtual environment to isolate the project's dependencies from your global Python environment. You can use the venv module to create a virtual environment:
  3. Activate the Virtual Environment using bash.
  4. Install Dependencies: Install the required dependencies (from requirements.txt file in the project repository) using pip.
  The requirements.txt file should list all the necessary packages, including Qiskit, NumPy, and Matplotlib. Additional libraries are optional but recommended.
  
## 3. Running the Code and simulating hypothesis ##


Once you've set up the environment, you can run the code by following these steps:
  
  1. Prepare the Input Data: The input data for the algorithm is a protein sequence, represented as a string of amino acid letters (e.g., "MVKETAFG..."). You can obtain protein sequences from various sources, such as the Protein Data Bank (PDB) or UniProt. You may also use your own data sources if desired.
  2. Create a QuantumEncoding object: Create an instance of the QuantumEncoding class, passing the desired protein sequence as an argument:
  3. Encode the Sequence: Encode the amino acid sequence into a quantum circuit using the encode() method:
  4. Generate Entanglement: Create an instance of the EntanglementLayer class, passing the quantum circuit as an argument, and apply the entanglement layer using the entangle() method:
  5. Perform Energy Minimization: Create an instance of the EnergyMinimization class, passing the entangled circuit and an energy function as arguments, and perform energy minimization using the minimize() method:
  6. Apply Intuitive Pattern Recognition: Create an instance of the IntuitiveLayer class, passing the optimized circuit and an initial state as arguments, and apply the intuitive layer using the apply_intuition() method:
  7. Measure and Interpret: Create an instance of the MeasurementAndInterpretation class, passing the final circuit as an argument, and measure and interpret the results using the measure_and_interpret() method:
  8. Visualize the Structure: Use the visualize_structure() function from the utils module to visualize the predicted 3D structure:


We hope this step-by-step guide provides a clear and concise overview of how to run the protein folding algorithm. If you need assistance or have questions regarding the code, please refer to section 5.5 - Communication and Support - below.

## 4. Interpreting the Results ##

Once you've run the code and obtained the predicted protein structure, you can interpret the results using various methods:

  1.Visualize the Structure: The visualize_structure() function in the utils.py module provides a basic 3D visualization of the protein structure. You can use this function to get an initial overview of the protein's shape and the relative positions of its atoms.
  
  2.Analyze Structural Properties: You can also calculate various structural properties of the predicted protein, such as its radius of gyration, solvent-accessible surface area, and secondary structure content. These properties can provide insights into the protein's stability, function, and potential interactions with other molecules.
  
  3. Compare with Experimental Data: If you have access to experimental data for the protein, such as X-ray crystallography or NMR data, you can compare the predicted structure to the experimental structure to assess the accuracy of the prediction.
     
  5. Evaluate the Energy Landscape: You can also explore the energy landscape of the protein folding process using the visualization tools provided in the visualization_tools.py module. This can help you to understand how the algorithm navigated the energy surface to find the predicted structure and to identify potential areas for improvement.
     
  7. Collaborate and Discuss: Share your findings and insights with other researchers and collaborators, engaging in discussions and brainstorming sessions to further analyze and interpret the results.



## 5. Communication and support ##
If you have any questions regarding the running of the code, interpreting the results, or feedback or ideas you’d like to share, please send a direct message to the Github account hosting this data, which you can access here. Alternatively, you can utilize the “Issues” feature on a specific file in the repository to ask a question or suggest a change. More support channels will be provided as the project progresses
While we strive to encourage full transparency and complete open-source information sharing in this project, we also respect the anonymity of our co-collaborators. Your messages will not be shared with any third party without your full consent.
Additionally, we welcome and encourage the development of a vibrant, transparent and passionate community for those wishing to contribute and share this project. Any participants are welcome to express their desire towards this goal and we will pledge to work with you to establish such a community if it is desired.
