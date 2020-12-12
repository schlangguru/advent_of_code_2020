# Importieren der Pygame-Bibliothek
import os
import pygame
from simulation import SeatPlan, SeatPlanSimulator

SCREEN_SIZE = (920, 940)

def init_sim():
    working_dir = os.path.dirname(__file__)
    input = os.path.join(working_dir, "input.txt")

    seats = []
    with open(input, 'r') as f:
        seats = [list(line.strip()) for line in f.readlines()]

    return SeatPlanSimulator(SeatPlan(seats), rule_set="part02")

def draw_seat_plan(screen, seat_plan):
    seat_witdh = int(SCREEN_SIZE[0] / seat_plan.width)
    seat_height = int(SCREEN_SIZE[1] / seat_plan.height)

    for seat_pos in seat_plan.traverse():
        x = seat_pos[0] * seat_witdh
        y = seat_pos[1] * seat_height
        colors = {
            "#": pygame.Color("#B00020"),
            "L": pygame.Color("#018786"),
            ".": pygame.Color("#212121")
        }
        pygame.draw.rect(screen, colors[seat_plan.get(seat_pos)], [x, y, seat_witdh, seat_height])


def main():
    pygame.init()

    # Open window
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Advent of Code - Day 11")

    # Clock for refresh time
    clock = pygame.time.Clock()
    simulator = init_sim()

    # Main loop
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False

        screen.fill((0,0,0))
        seat_plan = simulator.seat_plan
        draw_seat_plan(screen, seat_plan)

        pygame.display.update()

        simulator.simulate_round()
        simulator.simulate_round()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()


