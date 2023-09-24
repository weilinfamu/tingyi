def letter_frequency(message):
    freqs = {}
    message = message.upper()
    for i in message:
        # freqs[i] = freqs.get(i,0) + 1
        if i not in freqs:
            freqs = 0
        freqs[i] += 1
    return freqs