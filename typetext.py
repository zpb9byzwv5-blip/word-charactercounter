def count_text_stats(text):
  """Calculates word and character counts for a given text."""
  words = text.split()
  word_count = len(words)

  char_count_with_spaces = len(text)

  char_count_without_spaces = len("".join(words))

  return word_count, char_count_with_spaces, char_count_without_spaces

if __name__ == "__main__":
  print("=== Text Counter ===")
  user_input = input("Enter your text here:\n> ")
  words, chars_all, chars_no_space = count_text_stats(user_input)

  print("\n--- Results ---")
  print(f"Words:                       {words}")
  print(f"Characters (with spaces):    {chars_all}")
  print(f"Characters (without spaces): {chars_no_space}")
  print("--------------\n>")
