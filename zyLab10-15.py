# Name:Baichuan Chi
# PSID:1938207


class Team:
    def __init__(self, team_name='none', team_wins=0, team_losses=0):
        self.team_name = team_name
        self.team_wins = team_wins
        self.team_losses = team_losses

    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)

    def print_result(self):
        if self.get_win_percentage() > 0.5:
            print('Congratulations, Team', self.team_name, 'has a winning average!')
        else:
            print('Team', self.team_name, 'has a losing average.')


student_team = Team(input(), int(input()), int(input()))
student_team.print_result()