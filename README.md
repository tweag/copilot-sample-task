# Modus Create copilot evaluation tasks

This repository contains some Python tasks to help us evaluate the usefulness
of GitHub Copilot. Before proceeding, please ensure that you have access
to a Copilot subscription:

1. Sign in to your GitHub account
2. Go to https://github.com/settings/copilot and check whether you have an active subscription.

If you are a Modus Create employee and you don't have an active subscription, ping us on slack.

## Set up your development environment

We provide below two ways to set up your environment.

Codespaces is a managed environment where Visual Studio Code is installed, 
Copilot is configured and dependencies are installed.

If you cannot connect to Codespaces for any reason, use the manual installation
instructions.

### Option 1: Github Codespaces
To open this github repository in a python-enabled codespace, click the green
`<> Code` button and then click on the "Codespaces" tab. Click the "+" to create
a new codespace, and then wait for the editor to load. Even when the editor has
loaded, it may take another minute or two for the extensions to initialize.

<img src='images/create_codespace.png' width='350'>

If you are having trouble connecting or it's taking a long time, try signing in
from a different browser. If that does not work, use the manual instructions
below.

### Option 2: Manual setup
1. We assume you already have a Visual Studio Code instance with a Copilot
  extension and that you installed Python, Poetry, and git.
2. Open a terminal (or a command prompt or PowerShell window in Windows).
3. In the terminal, clone the Github repository:
  git clone git@github.com:tweag/copilot-draft-task.git
4. Navigate to the project’s root directory containing your `pyproject.toml` file.
5. Install the required packages with the command `poetry install`.

## Preliminaries
We assume some familiarity with Github/Git and Visual Studio Code.

Note: we do not consider this section as part of the 2 hour time estimate.
Please factor in more time if you need to go through the
resources below.

If you have not used Git before, take some time to familiarize yourself with
it first. Here are some resources we recommend:
- [Learn Git In 15 Minutes](https://www.youtube.com/watch?v=USjZcfj8yxE)
- [Git and GitHub Tutorial for Beginners](https://www.youtube.com/watch?v=tRZGeaHPoaw)

Visual Studio Code's basic usage is relatively esay and the interface is similar
in many ways to other IDEs. If it's your first time using Visual Studio Code and you
find the interface hard to navigate. Here are some tutorials to get you started:
- [Learn Visual Studio Code in 7min (Official Beginner Tutorial)](https://www.youtube.com/watch?v=B-s71n0dHUk&list=PLj6YeMhvp2S5UgiQnBfvD7XgOMKs3O_G6&index=1)
- [Using Git with Visual Studio Code (Official Beginner Tutorial)](https://www.youtube.com/watch?v=i_23KUAEtUM&list=PLj6YeMhvp2S5UgiQnBfvD7XgOMKs3O_G6&index=2)
- [Edit and Run Code in Visual Studio Code](https://www.youtube.com/watch?v=MNBwGGwvvKE&list=PLj6YeMhvp2S5UgiQnBfvD7XgOMKs3O_G6&index=3)

# Your task: basic data analysis with pandas and Streamlit

## Description
The file `diamonds.csv` contains data on diamond prices. It has the following
columns:

- carat: weight of the diamond (0.2--5.01)
- cut: quality of the cut (Fair, Good, Very Good, Premium, Ideal)
- color: diamond colour, from D (best) to J (worst)
- clarity: a measurement of how clear the diamond is (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best))
- price: price in US dollars ($326--$18,823)

The goal of this task is to aggregate, summarize, and visualize this data.

## Carry out data analysis and visualization
:warning: These tasks should be taken sequentially. Once done with a task,
commit your work as instructed below and do not come back to the task.
We will be using timestamps on commits to measure time spent on tasks so it's
important you do not revise your Git history after committing.

:bulb: Use Copilot as a complimentary tool to your usual development workflow.
It's totally fine to provide the answer if you know it, or to search the
internet or check the documentation. The exit survey will attempt to evaluate
how you used Copilot compared to these other tools.

The file `diamond_analysis/__init__.py` contains two functions that are not
yet implemented and several tests. You can use these tests to check up your
solution.
  
1. Create a branch with your github handle as follows:
  `git checkout -b <github-handle>-experiment`.
  This is very important as it will help us track your work.

2. Enter the virtual environment by typing `poetry shell` in the terminal.

3. Run the tests with `python -m unittest`. The first time you run the tests,
  they will understandably fail as the functions are not yet implemented.

4. To mark the start of your work, add your name and email in the authors field
  in `pyproject.toml` and save and commit your work with
  `git commit -m "Add name to contributors"`.

5. Complete the implementation of the `load()` function according to the
  function's documentation. You may find the pandas library useful.
  
  > :warning: Once done and the corresponding function test is passing, commit
  your work with `git commit -m "Implement the load() function"`

6. Complete the implementation of the `aggregate()` function according to the
  following documentation. You may copy and paste or prompt Copilot as you see fit.
    ```
    """Returns the average price of diamonds, restricted by a range of weights
    and grouped by a key.


    `weight_range` is a pair of numbers (the first smaller than the second) and
    `group_key` is one of "cut", "color", or "clarity". This function returns
    (as a list) the average price of diamonds whose weight is in the specified
    range (both endpoint included), divided into categories according to
    `group_key`.

    For example, if `weight_range` is `(0, 1)` and `group_key` is "cut"
    then the return value is a list of 5 elements. The first element is the
    average price of all diamonds weighing at most 1 carat and having a "Fair"
    quality cut; the next element is the average price of all diamonds weighing
    at most 1 carat and having a "Good" quality cut; and so on.
    The responses should be sorted by the quality of the cut (i.e. "Ideal"
    should come last).
    """
    ```
  
  > :warning: Once done and the corresponding function test is passing, commit
  your work with `git commit -m "Implement the aggregate() function"`

7. The unit tests do not cover the `filter_range()` function and they do not
  fully test the `aggregate()` function. Provide one suitable unit test for each
  function.
 
 > :warning: Once done, commit your work with `git commit -m "Add unit tests"`

8. The file `interactive.py` contains the stub of a data visualization. You can
  run it with the command

    ```sh
    streamlit run interactive.py
    ```

  Finish implementing this data visualization, by making the data in the bar
  chart depend on the selected carat range and choice of group.

  > :warning: Once done, commit your work with
  `git commit -m "Make bar chart depend on input selection"`

9. :stop_sign: **IMPORTANT**: **push** your work to the repository with
  `git push --set-upstream origin <your-branch-name>`

🤝 Examining how developers interact with Copilot is perhaps the best primary evidence we can study.
If you are OK sharing your **chat history** containing your interactions while doing the development tasks, please copy them to a **Google doc** _before_ closing your session.
You can provide us with the link in the exit survey.

We appreciate your time and effort!
