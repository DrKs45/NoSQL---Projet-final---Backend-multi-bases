import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import DashboardHome from './pages/DashboardHome';
import DeviceList from './pages/DeviceList';
import UserList from './pages/UserList';
import MaintenanceList from './pages/MaintenanceList';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<DashboardHome />} />
          <Route path="devices" element={<DeviceList />} />
          <Route path="users" element={<UserList />} />
          <Route path="maintenances" element={<MaintenanceList />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
