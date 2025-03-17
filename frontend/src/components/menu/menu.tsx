
import menu from "../menu/menu.module.css"


export default function Menu() {
  return (
    <div className={menu.menu}>
      <ul>
        <li>Add task</li>
        <li><a href="http://localhost:3000/">Today</a></li>
        <li><a href="http://facebook.com/">Upcoming</a></li>
        <li><a href="http://vg.no/">Search</a></li>
      </ul>
    </div>
  );
}