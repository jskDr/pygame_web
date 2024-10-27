import pygame
import asyncio

# Initialize Pygame
pygame.init()

# Set up the display
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Hello PyGame Web World!')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Set up font
font = pygame.font.SysFont(None, 48)
text = font.render('Hello PyGame Web World!', True, WHITE)
text_rect = text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/5))

async def main():
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Fill background
        screen.fill(BLACK)
        
        # Draw text
        screen.blit(text, text_rect)
        
        # Update display
        pygame.display.flip()
        
        # Required for web version
        await asyncio.sleep(0)

asyncio.run(main())