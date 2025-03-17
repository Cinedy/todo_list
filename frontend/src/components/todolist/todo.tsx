import styles from "../todolist/todo.module.css"

export default function Todo() {
    return (
        <div className={styles.todo}>
            <h2>Today</h2>
            <ul>
                <li>✅ Finish project setup</li>
                <li>📋 Add grid layout</li>
                <li>🛠️ Style components</li>
            </ul>
        </div>
    );
  }




