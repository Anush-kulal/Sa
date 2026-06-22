import React, { useState } from "react";

export default function ToDoFunction() {
  const [tasks, setTasks] = useState([]);
  const [task, setTask] = useState("");
  const add = () => {
    if (task) {
      setTasks([...tasks, { id: Date.now(), text: task, done: false }]);
      setTask("");
    }
  };

  return (
    <div style={{ textAlign: "center" }}>
      <h2>To-Do List</h2>
      <input value={task} onChange={(e) => setTask(e.target.value)} />
      <button onClick={add}>Add</button>
      <ul>
        {tasks.map(t => (
          <li key={t.id}>
            <span
              onClick={() => setTasks(tasks.map(x => x.id === t.id ? { ...x, done: !x.done } : x))}
              style={{ textDecoration: t.done ? "line-through" : "none" }}
            >
              {t.text}
            </span>
            <button onClick={() => setTasks(tasks.filter(x => x.id !== t.id))}>X</button>
          </li>
        ))}
      </ul>
    </div>
  );
}