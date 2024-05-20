# Substring Search Algorithm Performance Comparison

We compared the performance of Boyer-Moore, Knuth-Morris-Pratt (KMP), and Rabin-Karp algorithms on two articles with both existing and non-existing substrings.

## Results

### Article 1

- **Existing Substring**

  - Boyer-Moore: `0.008983`
  - KMP: `0.015315`
  - Rabin-Karp: `0.034797`

- **Non-Existing Substring**
  - Boyer-Moore: `0.004928`
  - KMP: `0.017029`
  - Rabin-Karp: `0.040387`

### Article 2

- **Existing Substring**

  - Boyer-Moore: `0.021101`
  - KMP: `0.040402`
  - Rabin-Karp: `0.069010`

- **Non-Existing Substring**
  - Boyer-Moore: `0.010413`
  - KMP: `0.019034`
  - Rabin-Karp: `0.068092`

## Conclusions

- **Boyer-Moore** is generally the fastest algorithm for existing substrings due to its ability to skip large sections of text.
- **Knuth-Morris-Pratt** provides consistent performance regardless of the substring's presence due to its preprocessing step.
- **Rabin-Karp** performs well with short patterns and is efficient for detecting multiple patterns but is slower compared to Boyer-Moore and KMP in this test.

Overall, the Boyer-Moore algorithm demonstrates the best performance in our tests, making it a preferred choice for substring search tasks in large texts.
