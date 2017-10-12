story = '''
Once when a lion, the king of the jungle, was asleep, a little mouse
 began running up and down on him. This soon awakened the lion, who
 placed his huge paw on the mouse, and opened his big jaws to swallow him.
'''


lion = input("Enter a animal:")
asleep = input("Enter a action:")
mouse = input("Enter a animal:")
running = input("Enter a action:")

story = story.replace("lion",lion)
story = story.replace("asleep",asleep)
story = story.replace("mouse",mouse)
story = story.replace("running",running)
print(story)
