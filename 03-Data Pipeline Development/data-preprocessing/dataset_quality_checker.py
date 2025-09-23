valid_chars = "\u0987\u0997\u0982\u09bc\u2019\u09c1\u0983\u09a8\u09e7\u099d\u09c2\u0993\u2018\u098a\u09cb\u099b\u09aa\u09ab\u09c8\u09ee\u09b7\u09af\u09ce\u09a2\u0988\u0995\u09a0\u09bf\u099c\u09e6\u09ec\u09c0\u099f\u09a1\u098f\u0985\u098b\u09a7\u099a\u09c7\u09e8\u09e9\u09a3\u0989\u09df\u09dd\u0996\u09b2\u09ad\u09d7\u09b8\u09b9\u09cd\u09dc\u09a6\u09a5\u09ac\u0994\u09be\u099e\u09b6\u09b0\u09cc\u09ae\u2014\u0990\u0986\u09c3\u0998\u0999\u200c\u0981\u09ea\u09eb\u09a4.?-!|, \u0964"

outliers = []

with open("metadata.txt", 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        parts = line.split('|')

        if len(parts) >= 3:
            audio_id = parts[0]
            text = parts[1]
            normalized_text = parts[2]

            reasons = []

            # Check for invalid characters
            invalid_chars = set()
            for char in text + normalized_text:
                if char not in valid_chars and char != ' ' and char != '\n' and char != '\r':
                    invalid_chars.add(char)

            if invalid_chars:
                reasons.append(f"invalid_chars: {''.join(invalid_chars)}")

            # Check if text equals normalized text
            if text != normalized_text:
                reasons.append("text_mismatch")

            if reasons:
                # Format: audio_id reason1 reason2
                outliers.append(f"{audio_id} {' '.join(reasons)}")

with open("outlier1.txt", 'w', encoding='utf-8') as outfile:
    outfile.write('\n'.join(outliers))