import random
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller

    Attributes:
        mistake_counter: tracks how many times the ball has collided with the bottom barrier.
    """
    def __init__(self):
        self.mistake_counter = 0    

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0] # there's only one
        paddles = cast["paddle"]
        bricks = cast["brick"]

        # Checking if the ball has hit the paddle.
        for paddle in paddles:
            if paddle.get_position().equals(ball.get_position()):
                ball._velocity._y = self._reverse(ball.get_velocity().get_y())
                break
        
        # Checking if the ball has hit any bricks.
        for brick in bricks:
            if brick.get_text() != "" and brick.get_position().equals(ball.get_position()):
                ball._velocity._y = self._reverse(ball.get_velocity().get_y())
                brick.set_text("")
                break
        
        # Checking if the ball has hit the bounderies.
        if ball.get_position().get_x() == constants.MAX_X -1 or ball.get_position().get_x() == 1:
            ball._velocity._x = self._reverse(ball.get_velocity().get_x())
        elif ball.get_position().get_y() == 1:
            ball._velocity._y = self._reverse(ball.get_velocity().get_y())       
        elif ball.get_position().get_y() == constants.MAX_Y - 1:
            self.mistake_counter += 1
            ball.set_position(Point(int(constants.MAX_X/2), int(constants.MAX_Y/2)))
            ball.set_velocity(Point(1,-1))
            if self.mistake_counter == constants.MAX_MISTAKES:
                quit()
            

    def _reverse(self,velocity):
        """Flips the passed in x or y velocity. Used to make the ball 'bounce'.
        Args:
            velocity: the velocity of the actor.
        """

        velocity = velocity * -1
        return velocity