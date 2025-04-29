def count_votes(ballots):
    """Count first-choice votes for each candidate."""
    vote_counts = {}  # Dictionary to store votes per candidate
    
    for ballot in ballots:
        if ballot:  # Ensure the ballot is not empty
            candidate = ballot[0]  # Take the first-choice candidate
            
            if candidate in vote_counts:
                vote_counts[candidate] += 1  # Increase count if candidate exists
            else:
                vote_counts[candidate] = 1  # Add candidate with first vote
    
    return vote_counts

def eliminate_candidate(ballots, candidate):
    """Remove the eliminated candidate from all ballots."""
    new_ballots = []
    
    for ballot in ballots:
        new_ballots.append([c for c in ballot if c != candidate])  # Remove the candidate from each ballot
    
    return new_ballots  # Return updated ballots

def instant_runoff(ballots):
    """Perform Instant Runoff Voting (IRV)"""
    while True:  # Repeat until a winner is found
        vote_counts = count_votes(ballots)  # Get first-choice vote counts
        total_votes = sum(vote_counts.values())  # Total number of votes

        # Check if any candidate has more than 50% of votes
        for candidate in vote_counts:
            if vote_counts[candidate] > total_votes / 2:
                return candidate  # This candidate wins!

        # Find the candidate(s) with the fewest votes
        min_votes = min(vote_counts.values())
        eliminated_candidates = [c for c in vote_counts if vote_counts[c] == min_votes]

        # Eliminate the least popular candidate(s)
        for candidate in eliminated_candidates:
            ballots = eliminate_candidate(ballots, candidate)

        # If all candidates are eliminated, return None (tie)
        if not any(ballots):
            return None

def process_input(user_input):
    """Converts user input string into a usable ballot format"""
    data = user_input.split()  # Split input string into list
    num_candidates = int(data[0])  # First value is the number of candidates
    num_voters = int(data[1])  # Second value is the number of voters
    votes = data[2:]  # Remaining values are the votes

    # Convert flat list into structured ballots
    ballots = [votes[i:i+num_candidates] for i in range(0, len(votes), num_candidates)]
    
    return ballots

# Read user input
user_input = input("Enter input (e.g., '2 5 a b a a b b b a b a'): ")
ballots = process_input(user_input)
winner = instant_runoff(ballots)
print(f"Winner: {winner}" if winner else "No winner (tie)")
