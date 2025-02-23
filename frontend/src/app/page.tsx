import styles from "../styles/page.module.css";
import Menu from "../components/menu/menu";
import Todo from "@/components/todolist/todo";

export default function Home() {
  return (
    <div className={styles.main}>
      <Menu />
      <Todo />
    </div>
  );
}

