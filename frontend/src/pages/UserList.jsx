import React, { useEffect, useState } from 'react';
import { fetchUsers } from '../api/client';
import { Users, Shield } from 'lucide-react';

const UserList = () => {
    const [users, setUsers] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetchUsers()
            .then(data => {
                setUsers(data);
                setLoading(false);
            })
            .catch(err => {
                console.error(err);
                setLoading(false);
            });
    }, []);

    if (loading) return <div>Loading users...</div>;

    return (
        <div className="card">
            <h2 style={{ marginBottom: '1.5rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                <Users size={24} color="var(--accent)" />
                User Management
            </h2>
            <table className="table">
                <thead>
                    <tr>
                        <th>Email</th>
                        <th>Role</th>
                        <th>Status</th>
                        <th>Created At</th>
                    </tr>
                </thead>
                <tbody>
                    {users.map(user => (
                        <tr key={user.id}>
                            <td style={{ fontWeight: 600 }}>{user.email}</td>
                            <td>
                                <span style={{ display: 'flex', alignItems: 'center', gap: '0.25rem' }}>
                                    <Shield size={14} /> {user.role}
                                </span>
                            </td>
                            <td>
                                {user.is_active ? (
                                    <span className="status-badge status-active">Active</span>
                                ) : (
                                    <span className="status-badge status-inactive">Inactive</span>
                                )}
                            </td>
                            <td style={{ color: 'var(--text-secondary)' }}>
                                {new Date(user.created_at).toLocaleDateString()}
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default UserList;
