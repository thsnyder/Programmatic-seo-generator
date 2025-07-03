import React from 'react'

export function Card({ children, className = '', ...props }) {
  return (
    <div className={`bg-white/90 backdrop-blur-sm rounded-xl shadow-lg border border-slate-200/50 ${className}`} {...props}>
      {children}
    </div>
  )
}

export function CardHeader({ children, className = '', ...props }) {
  return (
    <div className={`p-6 ${className}`} {...props}>
      {children}
    </div>
  )
}

export function CardTitle({ children, className = '', ...props }) {
  return (
    <h3 className={`text-xl font-semibold text-slate-900 ${className}`} {...props}>
      {children}
    </h3>
  )
}

export function CardContent({ children, className = '', ...props }) {
  return (
    <div className={`p-6 ${className}`} {...props}>
      {children}
    </div>
  )
} 