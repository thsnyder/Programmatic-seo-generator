import React from 'react'

export function Table({ children, className = '', ...props }) {
  return (
    <table className={`w-full border-collapse ${className}`} {...props}>
      {children}
    </table>
  )
}

export function TableHeader({ children, className = '', ...props }) {
  return (
    <thead className={`${className}`} {...props}>
      {children}
    </thead>
  )
}

export function TableBody({ children, className = '', ...props }) {
  return (
    <tbody className={`${className}`} {...props}>
      {children}
    </tbody>
  )
}

export function TableRow({ children, className = '', ...props }) {
  return (
    <tr className={`border-b border-slate-200/50 hover:bg-slate-50/30 transition-colors ${className}`} {...props}>
      {children}
    </tr>
  )
}

export function TableHead({ children, className = '', ...props }) {
  return (
    <th className={`px-4 py-4 text-left text-sm font-semibold text-slate-700 ${className}`} {...props}>
      {children}
    </th>
  )
}

export function TableCell({ children, className = '', ...props }) {
  return (
    <td className={`px-4 py-4 text-sm text-slate-900 ${className}`} {...props}>
      {children}
    </td>
  )
} 