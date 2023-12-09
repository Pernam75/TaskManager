import './App.css';
import React, { useEffect, useState } from 'react';


function App() {
  const [users, setUsers] = useState([]);
  const [tasks, setTasks] = useState([]);
  const [theme, setTheme] = useState(['business']);

  useEffect(() => {
    // Fetch user list from API
    fetch('http://localhost:4000/users', {
      method: 'GET',
    })
      .then(response => response.json())
      .then(data => setUsers(data.users))
      .catch(error => console.log(error));
  }, []);

  useEffect(() => {
    // Fetch task list from API
    fetch('http://localhost:4000/tasks', {
      method: 'GET',
    })
      .then(response => response.json())
      .then(data => setTasks(data.tasks))
      .catch(error => console.log(error));
  }, []);

  const refreshTasks = () => {
    fetch('http://localhost:4000/tasks', {
      method: 'GET',
    })
      .then(response => response.json())
      .then(data => setTasks(data.tasks))
      .catch(error => console.log(error));
  };

  const refreshUsers = () => {
    fetch('http://localhost:4000/users', {
      method: 'GET',
    })
      .then(response => response.json())
      .then(data => setUsers(data.users))
      .catch(error => console.log(error));
  };

  const AddTask = (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const data = {
      title: formData.get('title'),
      done: formData.get('done') === 'on',
      user_id: formData.get('user_id'),
    };
    fetch('http://localhost:4000/tasks', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    })
      .then(response => response.json())
      .then(data => {
        if (data.message === 'task created') {
          document.getElementById('my_modal_2').close();
          refreshTasks(); // Refresh tasks list by calling the API
        }
      })
      .catch(error => console.log(error));
  }

  const editTaskState = (id, done, title, user_id) => {
    const data = {
      title,
      done,
      user_id,
    };

    fetch(`http://localhost:4000/tasks/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    })
      .then(response => response.json())
      .then(data => {
        if (data.message === 'task updated') {
          setTasks(tasks.map(task => task.id === id ? { ...task, done } : task));
        }
      })
      .catch(error => console.log(error));
  }

  const editTask = (id, state) => (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const data = {
      title: formData.get('title'),
      done: formData.get('done') == state,
      user_id: formData.get('user_id'),
    };
    fetch(`http://localhost:4000/tasks/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    })
      .then(response => response.json())
      .then(data => {
        if (data.message === 'task updated') {
          refreshTasks(); // Refresh tasks list by calling the API
        }
      })
      .catch(error => console.log(error));
  }

  const deleteTask = (id) => {
    fetch(`http://localhost:4000/tasks/${id}`, {
      method: 'DELETE',
    })
      .then(response => response.json())
      .then(data => {
        if (data.message === 'task deleted') {
          setTasks(tasks.filter(task => task.id !== id));
          document.getElementById('my_modal_4').close();
        }
      })
      .catch(error => console.log(error));
  }

  const AddAccount = (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const data = {
      pseudo: formData.get('pseudo'),
      email: formData.get('email'),
      password: formData.get('password'),
    };
    fetch('http://localhost:4000/users', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    })
      .then(response => response.json())
      .then(data => {
        if (data.message === 'user created') {
          document.getElementById('my_modal_3').close();
          refreshUsers(); // Refresh tasks list by calling the API
        }
      })
      .catch(error => console.log(error));
  }


  return (
    <div className="App" data-theme={theme}>
      <div className="navbar bg-base-300">
        <div className="navbar-start">
          <div className="dropdown">
            <div tabIndex={0} role="button" className="btn btn-ghost btn-circle">
              <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 6h16M4 12h16M4 18h7" /></svg>
            </div>
            <ul tabIndex={0} className="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow bg-base-100 rounded-box w-52">
              <li><a onClick={() => document.getElementById('my_modal_3').showModal()}>Create account</a></li>
              <dialog id="my_modal_3" className="modal">
                <div className="modal-box">
                  <form className="py-4 flex flex-col" onSubmit={AddAccount}>
                    <h3 className="font-bold text-lg">Add New Account</h3>
                    <input type="text" name="pseudo" placeholder="Pseudo" className="mt-2 input input-bordered input-accent w-full " required />
                    <input type="email" name="email" placeholder="Email" className="mt-2 input input-bordered input-accent w-full" required />
                    <input type="password" name="password" placeholder="Password" className="mt-2 input input-bordered input-accent w-full" required />
                    <button type="submit" className="btn btn-accent mt-2">Add Account</button>
                  </form>
                </div>
                <form method="dialog" className="modal-backdrop">
                  <button>close</button>
                </form>
              </dialog>
              <li><a href="https://github.com/Pernam75/TaskManager" target='blank'>GitHub</a></li>
            </ul>
          </div>
        </div>
        <div className="navbar-center">
          <a className="btn btn-ghost text-xl">Task Manager</a>
        </div>
        <div className="navbar-end">

          <label className="swap swap-rotate">
            <input type="checkbox" onChange={(e) => setTheme(e.target.checked ? 'retro' : 'business')} />
            <svg className="swap-on fill-current w-5 h-5 mr-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M5.64,17l-.71.71a1,1,0,0,0,0,1.41,1,1,0,0,0,1.41,0l.71-.71A1,1,0,0,0,5.64,17ZM5,12a1,1,0,0,0-1-1H3a1,1,0,0,0,0,2H4A1,1,0,0,0,5,12Zm7-7a1,1,0,0,0,1-1V3a1,1,0,0,0-2,0V4A1,1,0,0,0,12,5ZM5.64,7.05a1,1,0,0,0,.7.29,1,1,0,0,0,.71-.29,1,1,0,0,0,0-1.41l-.71-.71A1,1,0,0,0,4.93,6.34Zm12,.29a1,1,0,0,0,.7-.29l.71-.71a1,1,0,1,0-1.41-1.41L17,5.64a1,1,0,0,0,0,1.41A1,1,0,0,0,17.66,7.34ZM21,11H20a1,1,0,0,0,0,2h1a1,1,0,0,0,0-2Zm-9,8a1,1,0,0,0-1,1v1a1,1,0,0,0,2,0V20A1,1,0,0,0,12,19ZM18.36,17A1,1,0,0,0,17,18.36l.71.71a1,1,0,0,0,1.41,0,1,1,0,0,0,0-1.41ZM12,6.5A5.5,5.5,0,1,0,17.5,12,5.51,5.51,0,0,0,12,6.5Zm0,9A3.5,3.5,0,1,1,15.5,12,3.5,3.5,0,0,1,12,15.5Z"/></svg>
            <svg className="swap-off fill-current w-5 h-5 mr-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M21.64,13a1,1,0,0,0-1.05-.14,8.05,8.05,0,0,1-3.37.73A8.15,8.15,0,0,1,9.08,5.49a8.59,8.59,0,0,1,.25-2A1,1,0,0,0,8,2.36,10.14,10.14,0,1,0,22,14.05,1,1,0,0,0,21.64,13Zm-9.5,6.69A8.14,8.14,0,0,1,7.08,5.22v.27A10.15,10.15,0,0,0,17.22,15.63a9.79,9.79,0,0,0,2.1-.22A8.11,8.11,0,0,1,12.14,19.73Z"/></svg>
          </label>
          
        </div>
      </div>

      <div class="flex flex-row h-screen">
        <div class="basis-1/5 bg-base-200 text-secondary-content p-10 flex-row">
          <button className="btn btn-accent w-full mb-5 text-primary-content" onClick={()=>document.getElementById('my_modal_2').showModal()}>Add Task</button>
          <dialog id="my_modal_2" className="modal">
            <div className="modal-box">
              <form className="py-4" onSubmit={AddTask}>
                <h3 className="font-bold text-lg">Add New Task</h3>
                <input type="text" name="title" placeholder="Task Title" className="mt-2 input input-bordered input-accent w-full" />
                <label className="block mt-2">
                  <input type="checkbox" name="done" className="mr-2" />
                  Done
                </label>
                <select name="user_id" className="select select-accent w-full mt-2 text-primary-content">
                  <option disabled selected className='text-primary-content'>Select user</option>
                  {users.map((user, index) => (
                    <option key={index} value={user.id} className='text-primary-content'>{user.pseudo}</option>
                  ))}
                </select>
                <button type="submit" className="btn btn-accent mt-2">Add Task</button>
              </form>
            </div>
            <form method="dialog" className="modal-backdrop">
              <button>close</button>
            </form>
          </dialog>

          <h1 className='text-primary-content'>Users</h1>

          <select className="select select-accent w-full mt-2 text-primary-content">
            <option disabled selected className='text-primary-content'>Select user</option>
            {users.map((user, index) => (
              <option key={index} className='text-primary-content'>{user.pseudo}</option>
            ))}
          </select>
          
        </div>

        
        <div class="grid grid-flow-row auto-rows-max basis-4/5 bg-base-100 text-primary-content px-5 overflow-auto">
          {tasks.map((task, index) => (
            <div>
              <div className="card bg-base-300 text-primary-content m-4">
                <div className="flex flex-row justify-between card-body">
                  <div className='flex flex-col'>
                    <h2 className="card-title">{task.title}</h2>
                    <div className={`badge ${task.done ? 'badge-success' : 'badge-error'} text-white gap-2`}>
                      {task.done ? 'Done' : 'Not Done'}
                    </div>
                  </div>
                  <div className="card-actions justify-end">
                    <button className={`btn ${task.done ? 'btn-error' : 'btn-success'} text-white`} onClick={() => editTaskState(task.id, !task.done, task.title, task.user_id)}>
                      {task.done ? 'Undo' : 'Done'}
                    </button>

                    <button className="btn btn-warning text-white" onClick={()=>document.getElementById('modify'+index).showModal()}>Modify</button>
                    {tasks.map((task, index) => (
                      <dialog id={'modify'+index} className="modal">
                        <div className="modal-box">
                          <h3 className="font-bold text-lg">Edit task !</h3>
                          <form onSubmit={editTask(task.id, task.done)}>
                            <input type="text" name="title" placeholder="Task Title" className="mt-2 input input-bordered input-accent w-full" />
                            <select name="user_id" className="select select-accent w-full mt-2 text-primary-content">
                              <option disabled selected className='text-primary-content'>Select user</option>
                              {users.map((user, index) => (
                                <option key={index} value={user.id} className='text-primary-content'>{user.pseudo}</option>
                              ))}
                            </select>
                            <button type="submit" className="btn btn-accent mt-2">Edit Task</button>
                          </form>
                        </div>
                        
                        <form method="dialog" className="modal-backdrop">
                          <button>close</button>
                        </form>
                      </dialog>
                    ))}

                    <button className="btn btn-error text-white" onClick={()=>document.getElementById('delete'+index).showModal()}>Delete</button>
                    {tasks.map((task, index) => (
                      <dialog id={'delete'+index} className="modal">
                        <div className="modal-box">
                          <h3 className="font-bold text-lg">Delete Task</h3>
                          <p className="mt-3">are you sure you want to delete this task ?</p>
                          <button className="mt-5 btn btn-error text-white" onClick={()=>deleteTask(task.id)}>Delete</button>
                        </div>
                        <form method="dialog" className="modal-backdrop">
                          <button>close</button>
                        </form>
                      </dialog>
                    ))}
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>

      </div>
    </div>
  );
}

export default App;
