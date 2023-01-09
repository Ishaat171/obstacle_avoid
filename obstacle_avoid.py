import pygame

# Initialize Pygame
pygame.init()

# Set the window size and caption
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Avoid the Obstacles")

# Set the character and obstacle images
character_image = pygame.image.load("C:/Users/ishaa/dojo/character.png")
obstacle_image = pygame.image.load("C:/Users/ishaa/dojo/obstacle.png")

# Set the character and obstacle positions
character_x = 320
character_y = 240
obstacle_x = 640
obstacle_y = 240

# Set the character and obstacle speeds
character_speed = 0
obstacle_speed = -5

# Set the game clock
clock = pygame.time.Clock()

# Run the game loop
while True:
  # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  # Update the character speed based on arrow key presses
  pressed_keys = pygame.key.get_pressed()
  if pressed_keys[pygame.K_UP]:
    character_speed = -5
  elif pressed_keys[pygame.K_DOWN]:
    character_speed = 5
  else:
    character_speed = 0

  # Update the character position
  character_y += character_speed

  # Update the obstacle position
  obstacle_x += obstacle_speed

  # If the obstacle goes off the screen, reset its position
  if obstacle_x < -64:
    obstacle_x = 640

  # Draw the character and obstacle
  screen.blit(character_image, (character_x, character_y))
  screen.blit(obstacle_image, (obstacle_x, obstacle_y))

  # Update the display
  pygame.display.flip()

  # Limit the frame rate to 60 FPS
  clock.tick(60)