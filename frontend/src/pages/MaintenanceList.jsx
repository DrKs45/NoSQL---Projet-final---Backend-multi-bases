import React, { useEffect, useState } from 'react';
import { fetchMaintenances } from '../api/client';
import { Wrench, Clock, AlertCircle } from 'lucide-react';

const MaintenanceList = () => {
    const [maintenances, setMaintenances] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetchMaintenances()
            .then(data => {
                setMaintenances(data);
                setLoading(false);
            })
            .catch(err => {
                console.error(err);
                setLoading(false);
            });
    }, []);

    if (loading) return <div>Loading maintenances...</div>;

    const getStatusStyle = (status) => {
        switch (status) {
            case 'completed': return 'status-active';
            case 'planned': return 'status-warning';
            case 'in_progress': return 'status-active'; // Or blue
            default: return 'status-inactive';
        }
    };

    return (
        <div className="card">
            <h2 style={{ marginBottom: '1.5rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                <Wrench size={24} color="var(--accent)" />
                Maintenance Schedule
            </h2>
            <table className="table">
                <thead>
                    <tr>
                        <th>Description</th>
                        <th>Device ID</th>
                        <th>Status</th>
                        <th>Start Time</th>
                        <th>End Time</th>
                    </tr>
                </thead>
                <tbody>
                    {maintenances.map(item => (
                        <tr key={item.id}>
                            <td style={{ fontWeight: 600 }}>{item.description}</td>
                            <td>#{item.device_id}</td>
                            <td>
                                <span className={`status-badge ${getStatusStyle(item.status)}`}>
                                    {item.status}
                                </span>
                            </td>
                            <td style={{ fontSize: '0.875rem' }}>
                                {item.start_time ? new Date(item.start_time).toLocaleString() : '-'}
                            </td>
                            <td style={{ fontSize: '0.875rem' }}>
                                {item.end_time ? new Date(item.end_time).toLocaleString() : '-'}
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default MaintenanceList;
