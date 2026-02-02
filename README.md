𝐑𝐚𝐧𝐝𝐨𝐦 𝐍𝐮𝐦𝐛𝐞𝐫 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐨𝐫 𝐂𝐨𝐦𝐩𝐚𝐫𝐢𝐬𝐨𝐧
𝐗𝐨𝐫𝐬𝐡𝐢𝐟𝐭 𝐯𝐬. 𝐌𝐞𝐫𝐬𝐞𝐧𝐧𝐞 𝐓𝐰𝐢𝐬𝐭𝐞𝐫 (𝐏𝐲𝐭𝐡𝐨𝐧 & 𝐉𝐚𝐯𝐚)

📌 𝐎𝐯𝐞𝐫𝐯𝐢𝐞𝐰

As we move toward an era of highly globalized virtual systems driven by AI-powered connectedness, technologies such as Cloud Computing, Data Analytics, Generative AI, Blockchain, and the Internet of Things (IoT) are becoming increasingly important. Many modern applications—such as simulation, gaming, cybersecurity, and scientific computing—depend heavily on efficient and high-quality random number generation.

This repository presents a comparative study of two widely used non-cryptographic Pseudo Random Number Generators (PRNGs):

XORshift

Mersenne Twister (MT19937)

The implementations are designed to analyze their performance, statistical behavior, collision thresholds, and execution speed, with a focus on practical usability across different programming environments.

🎯 𝐎𝐛𝐣𝐞𝐜𝐭𝐢𝐯𝐞𝐬

Compare XORshift and Mersenne Twister PRNGs

Analyze performance across different sample sizes (from small samples to very large datasets)

Study frequency distribution and collision behavior

Evaluate execution speed and implementation efficiency

Provide insights into language-based performance differences (Python vs Java)

🔬 Algorithms Included
1️⃣ 𝐗𝐎𝐑𝐬𝐡𝐢𝐟𝐭 (𝐗𝐨𝐫𝐬𝐡𝐢𝐟𝐭𝟏𝟐𝟖)

XORshift is a family of PRNGs that generates randomness using bitwise XOR and shift operations.

Key characteristics:

128-bit internal state

Extremely fast

Small memory footprint

Suitable for simulations and performance-critical applications

State transition:
<img width="407" height="108" alt="image" src="https://github.com/user-attachments/assets/6c455c1d-3539-42df-a8f9-3a6f8bf6a370" />


2️⃣ 𝐌𝐞𝐫𝐬𝐞𝐧𝐧𝐞 𝐓𝐰𝐢𝐬𝐭𝐞𝐫 (𝐌𝐓𝟏𝟗𝟗𝟑𝟕)

The Mersenne Twister is one of the most widely used PRNGs and is the default random number generator in Python.

Key characteristics:

Period of 2^19937−1

State vector of 624 32-bit integers

High statistical quality

Commonly used in scientific simulations and modeling

🛠 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬

✅ Dual-Algorithm Support (XORshift & Mersenne Twister)

📊 Frequency Distribution Analysis using collections.Counter

🖥 Formatted Terminal Output for easy readability

📁 File Export of generated numbers and frequency counts

⚙️ Configurable sample size for experimentation

📂 Repository Contents

Python implementation of XORshift128

Python implementation using Mersenne Twister

Frequency analysis and result export

(Java implementations can be added or linked if applicable)

▶️ How to Run
Prerequisites

Python 3.x installed

Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Run the Script
python xorshift11.py

Follow On-Screen Prompts

Enter the total number of random numbers to generate

Choose:

1 for XORshift128

2 for Mersenne Twister

📄 Output

A sample of generated random numbers is displayed in the terminal

Full output is saved to random_numbers.txt

Frequency count of each generated number is included

Example Output
123456789   987654321   456123789   ...
Frequency of each number:
123456789 : 1
987654321 : 1

📊 Experimental Insights

XORshift demonstrates very high speed with minimal overhead

Mersenne Twister provides excellent statistical quality

Java implementations consistently outperform Python in execution speed

Performance varies significantly with dataset size and platform

📌 Applications

Scientific simulations

Monte Carlo methods

Gaming systems

Non-cryptographic security models

Performance benchmarking of PRNGs

🧠 Conclusion

This comparative analysis offers practical guidance for selecting an appropriate PRNG and programming language based on:

Dataset size

Performance requirements

Platform constraints

The results are especially useful for new researchers and developers working with large-scale simulations and randomness-dependent applications.

🔑 Keywords

Random Number Generation, XORshift, Mersenne Twister, Python, Java, Collision Threshold, Execution Time, PRNG
