import React, { useEffect, useState } from 'react';
import { fetchDevices, fetchUsers, fetchMaintenances } from '../api/client';
import { Server, Users, Wrench, Activity } from 'lucide-react';

const StatCard = ({ title, value, icon: Icon, color }) => (
    <div className="card" style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <div>
            <div style={{ color: 'var(--text-secondary)', fontSize: '0.875rem', marginBottom: '0.5rem' }}>{title}</div>
            <div style={{ fontSize: '2rem', fontWeight: 700 }}>{value}</div>
        </div>
        <div style={{ padding: '1rem', borderRadius: '1rem', background: `rgba(${color}, 0.1)`, color: `rgb(${color})` }}>
            <Icon size={32} />
        </div>
    </div>
);

const DashboardHome = () => {
    const [stats, setStats] = useState({ devices: 0, users: 0, maintenances: 0 });
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        Promise.all([fetchDevices(), fetchUsers(), fetchMaintenances()])
            .then(([devices, users, maintenances]) => {
                setStats({
                    devices: devices.length,
                    users: users.length,
                    maintenances: maintenances.length
                });
                setLoading(false);
            })
            .catch(err => {
                console.error(err);
                setLoading(false);
            });
    }, []);

    if (loading) return <div>Loading dashboard...</div>;

    return (
        <div>
            <div style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))',
                gap: '1.5rem',
                marginBottom: '2rem'
            }}>
                <StatCard title="Total Devices" value={stats.devices} icon={Server} color="59, 130, 246" />
                <StatCard title="Active Users" value={stats.users} icon={Users} color="16, 185, 129" />
                <StatCard title="Planned Maintenances" value={stats.maintenances} icon={Wrench} color="245, 158, 11" />
                <StatCard title="System Status" value="Healthy" icon={Activity} color="236, 72, 153" />
            </div>

            <div className="card">
                <h3>System Overview</h3>
                <p style={{ color: 'var(--text-secondary)', marginTop: '1rem' }}>
                    Welcome to the NetOps Inventory Dashboard. Use the sidebar to navigate through the different modules.
                </p>
            </div>
        </div>
    );
};

export default DashboardHome;
