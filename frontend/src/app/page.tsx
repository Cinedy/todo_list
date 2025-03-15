import styles from "./page.module.css";
import Todo from "@/components/todolist/todo";

export default function Home() {
  return (
    <div className={styles.pageContent}>
      <Todo />
    </div>
  );
}