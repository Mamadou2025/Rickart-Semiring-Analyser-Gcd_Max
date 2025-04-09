# Endomorphism Semiring and Rickart Properties

This Python script analyzes the structure of the endomorphism semiring over a set \( M \), determining whether the semiring exhibits i-Rickart and w-Rickart properties.

## Overview

The script defines several functions that:
- Check whether a function preserves the greatest common divisor (GCD) operation (`is_endomorphism`).
- Determine if a function is idempotent (`is_idempotent`).
- Compute function composition (`compose`).
- Compute the subtractive closure of a semiring (`subtractive_closure`).
- Check whether the semiring satisfies i-Rickart and w-Rickart properties (`is_i_rickart`, `is_w_rickart`).
- Generate all valid endomorphisms and test the Rickart properties (`test_s_rickart`).

## Installation

Ensure you have Python installed. This script does not require additional dependencies beyond Python's standard library.

## Usage

Run the script with:

```bash
python script.py
