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

    return SeatPlanSimulator(SeatPlan(seats), rule_set="part01")

def draw_seat_plan(screen, seat_plan):
    seat_witdh = int(SCREEN_SIZE[0] / seat_plan.width)
    seat_height = int(SCREEN_SIZE[1] / seat_plan.height)

    for seat_pos in seat_plan.traverse():
        x = seat_pos[0] * seat_witdh
        y = seat_pos[1] * seat_height
        seat = seat_plan.get(seat_pos)

        color = pygame.Color("#212121") # Floor
        if seat:
            if seat.is_occupied:
                color = pygame.Color("#B00020")
            else:
                color = pygame.Color("#00C853")

        pygame.draw.rect(screen, color, [x, y, seat_witdh, seat_height])


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
    run_sim = False
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    run_sim = True

        screen.fill((0,0,0))
        seat_plan = simulator.seat_plan
        draw_seat_plan(screen, seat_plan)

        pygame.display.update()

        if run_sim:
            simulator.simulate_round()
            updates = simulator.simulate_round()
            if len(updates) == 0:
                simulator = init_sim()

        clock.tick(20)

    pygame.quit()

if __name__ == "__main__":
    main()


