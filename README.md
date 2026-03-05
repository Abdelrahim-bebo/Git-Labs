# Git History & Undo Lab 🛠️

## Objective 🎯
This lab demonstrates advanced Git version control techniques, including local repository initialization, history manipulation (Reset, Amend, Revert), and remote synchronization using SSH.

## Lab Execution Log ✅

### 1. Environment Setup
* **SSH Configuration**: Generated a new Ed25519 key pair and authenticated with GitHub.
* **Initialization**: Created `python_project` directory and initialized a new Git repository.
* **Branching**: Default branch set to `main`.

### 2. History Manipulation
* **Phase 1 (Populating)**: Created `script.py` and made 4 distinct commits involving task list updates and comment removals.
* **Phase 2 (The Reset)**: Executed `git reset --hard HEAD~2` to jump back to commit `552bac0`, removing the two most recent changes from the timeline.
* **Phase 3 (The Recovery)**: Added a new change and committed with the message `"Commit after deletion"`.
* **Phase 4 (The Amend)**: Used `git commit --amend -m "finish"` to fix the last commit, incorporating the "lab Done" changes into the existing commit history.
* **Phase 5 (The Revert)**: Used `git revert HEAD~1` to safely undo a previous change by creating a new inverse commit.

### 3. Remote Integration
* **Remote Link**: Added origin `git@github.com:Abdelrahim-bebo/Git-Labs.git`.
* **Deployment**: Successfully pushed the local `main` branch to GitHub using `git push -u origin main`.

## Key Commands Used 💻
| Task | Command |
| :--- | :--- |
| **Undo last 2 commits** | `git reset --hard HEAD~2` |
| **Fix last commit message/code** | `git commit --amend -m "new message"` |
| **Safe undo (Inverse commit)** | `git revert HEAD~1` |
| **Check history** | `git log --oneline` |
| **Push to GitHub** | `git push -u origin main` |

---
**Status**: Lab Completed Successfully 🚀
