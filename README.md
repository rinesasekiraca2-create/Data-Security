# Breaking Caesar Cipher using Frequency Analysis



## Overview

This project demonstrates a practical method for breaking the Caesar Cipher using frequency analysis. Instead of relying solely on brute force, the approach evaluates how closely decrypted text matches the statistical patterns of natural English.



It highlights a key concept in cryptography: encryption methods that preserve patterns are inherently vulnerable.



## Core Idea

Although the Caesar Cipher shifts letters, it does not change how frequently letters appear. Since English has a predictable distribution of characters, this property can be exploited.



The system:

- Tries all possible shifts (0–25)

- Analyzes letter frequencies for each result

- Compares them with a reference English text

- Selects the most likely plaintext based on similarity



## Project Structure

- file_utils.py → File handling (reading & writing)

- frequency.py → Letter frequency calculation

- caesar.py → Encryption and decryption logic

- attack.py → Statistical analysis and key detection

- main.py → Program execution and coordination



## Methodology



### Reference Modeling

A reference English text is used to establish expected letter patterns.



### Brute Force Decryption

The encrypted text is decrypted using all possible shifts.



### Statistical Comparison

Each result is evaluated based on how closely it resembles natural English.



### Best Match Selection

The most statistically similar result is selected as the correct decryption.



## Execution

Run the program with:



python main.py



The program will:

- Display frequency analysis

- Evaluate all possible shifts

- Output the most probable plaintext

- Save the result in output.txt



## Contributors

- Diona Gërxhaliu → File handling & frequency analysis

- Elsa Shaqiri → Caesar cipher implementation

- Rinesa Sekiraça → Attack logic and statistical evaluation

- Djellza Ramaja → Integration and main execution



## Key Takeaways

- The Caesar Cipher is insecure due to its limited key space

- Language patterns make encrypted text predictable

- Statistical analysis is a powerful tool in cryptanalysis



## Conclusion

This project illustrates how mathematics, programming, and linguistic patterns can be combined to break classical encryption methods, reinforcing the importance of stronger modern cryptographic techniques.

