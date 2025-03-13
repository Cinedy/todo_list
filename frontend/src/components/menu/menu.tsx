
import menu from "../menu/menu.module.css"


export default function Menu() {
  return (
    <div className={menu.menu}>
      <div>Add task</div>
      <div>Today</div>
      <div>Upcoming</div>
    </div>
  );
}