import React from 'react'

export function Select({ value, onChange, options, placeholder, className = "" }) {
  return (
    <select
      value={value}
      onChange={(e) => onChange(e.target.value)}
      className={`w-full px-3 py-2 border border-files-light-pink rounded-md focus:border-files-primary-red focus:ring-files-primary-red/20 transition-all bg-white ${className}`}
    >
      <option value="">{placeholder}</option>
      {options.map((option) => (
        <option key={option.value} value={option.value}>
          {option.label}
        </option>
      ))}
    </select>
  )
} 