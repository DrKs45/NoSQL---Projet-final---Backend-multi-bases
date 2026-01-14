import React from 'react';
import { NavLink, Outlet } from 'react-router-dom';
import { LayoutDashboard, Server, Users, Wrench } from 'lucide-react';
import '../App.css';

const Layout = () => {
    return (
        <div className="layout">
            <aside className="sidebar">
                <div className="sidebar-title">
                    <LayoutDashboard size={28} />
                    <span>NetOps</span>
                </div>
                <nav>
                    <NavLink to="/" className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}>
                        <LayoutDashboard size={20} /> Dashboard
                    </NavLink>
                    <NavLink to="/devices" className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}>
                        <Server size={20} /> Devices
                    </NavLink>
                    <NavLink to="/users" className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}>
                        <Users size={20} /> Users
                    </NavLink>
                    <NavLink to="/maintenances" className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}>
                        <Wrench size={20} /> Maintenances
                    </NavLink>
                </nav>
            </aside>
            <main className="main-content">
                <div className="header">
                    <h1 className="page-title">NetOps Manager</h1>
                </div>
                <Outlet />
            </main>
        </div>
    );
};

export default Layout;
