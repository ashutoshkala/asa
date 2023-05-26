def hamming_code(data):
  """
  Encodes the given data using the Hamming code.

  Args:
    data: The data to be encoded.

  Returns:
    The encoded data.
  """

  # Calculate the number of parity bits.
  n = len(data)
  k = n - 1
  r = len(bin(k)) - 2

  # Create a list of parity bits.
  parity_bits = [0] * r

  # Calculate the values of the parity bits.
  for i in range(r):
    parity_bits[i] = sum(data[i::2]) % 2

  # Return the encoded data.
  return data + parity_bits


def hamming_decode(data):
  """
  Decodes the given data using the Hamming code.

  Args:
    data: The data to be decoded.

  Returns:
    The decoded data.
  """

  # Check if the data is valid.
  if len(data) % 2 == 1:
    raise ValueError("The data must be a multiple of 2.")

  # Calculate the number of parity bits.
  n = len(data)
  k = n - 1
  r = len(bin(k)) - 2

  # Create a list of parity bits.
  parity_bits = [0] * r

  # Calculate the values of the parity bits.
  for i in range(r):
    parity_bits[i] = sum(data[i::2]) % 2

  # Check if there are any errors.
  for i in range(r):
    if parity_bits[i] != data[i + k]:
      data[i + k] = 1 - data[i + k]

  # Return the decoded data.
  return data[:k]
