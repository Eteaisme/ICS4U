# Function to evaluate our policy against itself
import numpy as np
def policy_evaluation_q(policy, theta=1e-3):
    '''
    Performs iterative policy evaluation for a given policy against another policy.
    Parameters:
        policy: The policy being evaluated.
        theta: A small value we use to decide when IPE has converged.
    Returns:
        Q: The action-value function as a numpy array dimensions [i, j, k, a].
        delta_list: A list of maximum probability updates for a given iteration of IPE.
    '''
    # Initialize the action-value function ar
    Q = np.zeros((100 + 6, 100 + 6, 100 + 6, 2))

    # Initial delta
    delta = 1 

    # We store all computed max deltas for plotting later
    delta_list = []

    while delta > theta:
        delta = 0
        # Copy old values to calculate change later
        Q_old = Q.copy()

        for i in reversed(range(100 + 6)): # Backward induction
            for j in reversed(range(100 + 6)):
                for k in reversed(range(100 + 6)):
                    
                    # Terminal states
                    if i + k >= 100:
                        Q[i, j, k, 0] = 1.0
                        continue
                    elif j >= 100:
                        Q[i, j, k, :] = 0.0
                        continue
                        
                    # Non-terminal states
                    # Q-values for us holding
                    next_choice = policy[j, min(100, i + k), 0]
                    Q[i, j, k, 0] = 1 - Q[j, min(100, i + k), 0, next_choice]

                    # Q-values for us rolling
                    next_choice = policy[j, i, 0]
                    v_roll = (1 - Q[j, i, 0, next_choice]) / 6  # Rolling a 1
                    for roll in range(2, 7):  # Rolling 2, 3, 4, 5, 6
                        next_choice = policy[i, j, min(100, k + roll)]
                        v_roll += Q[i, j, min(100, k + roll), next_choice] / 6
                    Q[i, j, k, 1] = v_roll

                    # Update delta
                    delta = max(delta, sum(abs(Q_old[i, j, k, :] - Q[i, j, k, :]))/2)

        delta_list.append(delta)

    return Q, delta_list

# Policy improvement
def update_policy(policy, Q):
    '''
    Takes in a policy and a Q function, and updates the policy so it uses 
    the move with the largest Q-value.
    Parameters:
        policy: A numpy array of shape (106, 106, 106) indicating whether to hold or roll (0 or 1) for each game state.
        Q: The state-action value function indicating the probability of winning for taking an action in each game state.
    Returns:
    policy: The updated policy.
    '''
    old_policy = policy.copy()
    new_policy = policy.copy()
    
    for i in range(policy.shape[0]):
        for j in range(policy.shape[1]):
            for k in range(policy.shape[2]):
                new_policy[i, j, k] = np.argmax(Q[i,j,k,:])
    
    changes = old_policy - new_policy
    num_updated_actions = np.count_nonzero(changes)
    return new_policy, num_updated_actions

def plot_generalized_policy_iteration_convergence(num_updates, title = ""):
    '''
    Plots a line graph showing convergence of generalized policy iteration.
    Parameters:
        num_updates: A list containing the number of parameters updated for each iteration of GPI.
    '''
    # Create a line plot
    fig = go.Figure()

    # Add trace
    fig.add_trace(go.Scatter(
        y=num_updates,  # Number of action updates on y-axis
        mode='lines+markers',  # Line plot with markers
        marker=dict( # Configuring markers
            size=8,  
            color='#00CC96',
        ),
        line=dict( # Configuring line
            width = 3,
            color='#00CC96',  
        ),
        hovertemplate='Iterations: %{x}<br>Number of Actions Updated: %{y}',  # Custom hover template
        name='Number of Updates',  # Name of the trace
    ))

    # Set title and labels
    fig.update_layout(
        title='Generalized Policy Iteration Convergence ' + title,
        xaxis_title='Iterations',
        yaxis_title='Number of Actions Updated',
    )

    # Show the plot
    fig.show()
    

# Hold at 20 policy for opponent:
hold_at_20_policy = np.zeros((106, 106, 106)).astype(int)
# Define the policy where we roll when k < 20 and i + k < 100
for i in range(100 + 6):
    for j in range(100 + 6):
        for k in range(100 + 6):
            if k < 20 and i + k < 100:
                hold_at_20_policy[i, j, k] = 1  # 1 represents 'roll'
                
policy = hold_at_20_policy.copy()
theta = 1e-3
Q, delta_list = policy_evaluation_q(policy, theta=theta) # Allow for max 0.1% convergence update for time reasons
plot_policy_evaluation_convergence(delta_list, f"- Hold at 20 Policy Q Function Evaluation (theta={theta})")
policy, num_updates = update_policy(policy, Q)
print("Number of actions updated:", num_updates)
print("\nDemonstration of policy improvement:")
example_state = (79, 99, 20)
print(f"Old policy: state = (79, 99, 20), action = {hold_at_20_policy[example_state]}")
print(f"New policy: state = (79, 99, 20), action = {policy[example_state]}")
print("The new policy performs an obvious 'roll' whereas 'hold at 20' follows the rule obsequiously.")