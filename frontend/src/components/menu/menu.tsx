
import menu from "../menu/menu.module.css"


export default function Menu() {
  return (
    <div className={menu.menu}>
      <menu className={menu.menu}>
        <div>Add task</div>
        <div>Today</div>
        <div>Upcomming</div>
      </menu>
    </div>
  );
}